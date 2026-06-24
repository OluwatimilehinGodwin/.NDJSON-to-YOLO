#this script converts an ndjson dataset to a YOLO dataset format using the Ultralytics library.

import asyncio
from ultralytics.data.converter import convert_ndjson_to_yolo

async def main():
    yaml_path = await convert_ndjson_to_yolo(
        r"Ultralytics-dataset.ndjson", #path to the input ndjson file
        output_path=r"dataset" #path to save the converted dataset in folder format
    )
    print(f"Dataset saved to: {yaml_path}")

asyncio.run(main())