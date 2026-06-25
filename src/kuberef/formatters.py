import json
import sys

def stream_ndjson_event(event_data: dict):
    """
    Serializes a dictionary to NDJSON format and writes it to stdout.
    """
    try:
        # Convert the event dictionary to a JSON string
        ndjson_line = json.dumps(event_data)
        
        # Write to stdout followed by a newline
        sys.stdout.write(ndjson_line + '\n')
        
        # Ensure the stream is flushed immediately
        sys.stdout.flush()
    except (TypeError, ValueError) as e:
        sys.stderr.write(f"Error serializing event to NDJSON: {e}\n")

def emit_ndjson(event_type: str, data: dict):
    """
    Flattens data into a single-line JSON string with an event discriminator.
    """
    payload = {"event": event_type}
    payload.update(data)
    # separators=(',', ':') removes all spaces, ensuring strict single-line format
    print(json.dumps(payload, separators=(',', ':')))