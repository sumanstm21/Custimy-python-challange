import aiohttp
import json
import asyncio
import argparse

API_URL = "https://api.agify.io"

async def get_age(session, names, country_id=None):
    params = {"name[]": names}
    if country_id:
        params["country_id"] = country_id
    
    # GET Request
    try:
        url = f"{API_URL}"
        # print(f"API URL: {url}")
        
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            data = await response.json()    
            return data
    except aiohttp.ClientError as e:
        print(f"Error fetching data: {e}")
        return []

async def main(input_file, output_file, country_id):
    async with aiohttp.ClientSession() as session:
        with open(input_file, 'r') as f:
            people_data = json.load(f)
            names = [person['name'] for person in people_data]
            emails = [person['email'] for person in people_data]

        results = []
        batch_size = 10

        for i in range(0, len(names), batch_size):
            name_batch = names[i:i+batch_size]
            batch_result = await get_age(session, name_batch, country_id)
            results.extend(batch_result)

        # Filtering Output
        processed_results = [{'email': email, 'name': name, 'age': entry.get('age')} for email, name, entry in zip(emails, names, results)]
        for email, name, entry in zip(emails, names, results):
            age = entry.get('age')
            if age is not None:
                processed_results.append({'email': email, 'name': name, 'age': age})

        with open(output_file, 'w') as f:
            json.dump(processed_results, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Predict the age of names.')
    parser.add_argument('input_file', type=str, help='input JSON file')
    parser.add_argument('output_file', type=str, help='output JSON file')
    parser.add_argument('--country_id', type=str, help='country code for localization')
    args = parser.parse_args()
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(args.input_file, args.output_file, args.country_id))
