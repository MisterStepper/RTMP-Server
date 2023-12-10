import sys

def toggle_youtube_stream(config_file_path, toggle_option):
    youtube_stream_key = "# stream_key = ip/live/test"  # Replace with your actual YouTube stream key line
    default_stream_key = "stream_key = ip/live/test"  # Replace with your actual default stream key line

    with open(config_file_path, 'r') as file:
        config_data = file.read()

    # Check the toggle option
    if toggle_option == 'on':
        updated_config = config_data.replace(default_stream_key, youtube_stream_key)
        print("Switching to YouTube stream.")
    elif toggle_option == 'off':
        updated_config = config_data.replace(youtube_stream_key, default_stream_key)
        print("Switching to default stream.")
    else:
        print("Invalid toggle option. Use 'on' or 'off'.")
        return

    with open(config_file_path, 'w') as file:
        file.write(updated_config)

# Specify the path to your RTMP server config file
config_file_path = "/path/to/your/config/file.conf"  # Replace with the actual path

# Specify the toggle option ('on' for YouTube, 'off' for default)
toggle_option = sys.argv[1] if len(sys.argv) > 1 else None

# Run the script to toggle the YouTube stream
toggle_youtube_stream(config_file_path, toggle_option)
