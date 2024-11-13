# Netfly Subtitle Converter - The XML Approach

**Netfly Subtitle Converter** is a tool for converting Japanese subtitles to English ( currently hardcoded ) on Netflix, particularly useful when English subtitles aren’t available.

## Overview

This tool leverages Netflix’s XML subtitle files to directly access Japanese text, which is then translated to English using AWS Translate. By accessing subtitles from the XML file, we bypass the need for computer vision ( which was a part of my iteration 1 ), making the process more efficient and cost-effective.

## Approach

1. **Subtitle Extraction**: The tool retrieves the XML subtitle file from Netflix, containing Japanese subtitle text along with precise start and end times for each line.
2. **XPath Navigation**: Using XPath, we traverse the XML to extract each subtitle line, including its timing information.
3. **Translation**: The extracted Japanese text is sent to AWS Translate for English translation.
4. **Subtitle Syncing**: The translated English subtitles are synced with the original video timing for seamless viewing.

## Features

- **Efficient Translation**: Directly accesses subtitle text in XML format, reducing resource usage by avoiding computer vision.
- **Real-Time Syncing**: Matches translated subtitles with the original timing data in the XML file.
- **Scalable**: Optimized for performance, making it suitable for frequent use without high costs.

## Future Enhancements

Currently, the subtitle XML file must be manually downloaded from Netflix. I'm working on a Playwright script to automate this step, streamlining the entire subtitle conversion process.

## Working Demo / Screenshots

<img width="1120" alt="Screenshot 2024-11-13 at 8 01 33 PM" src="https://github.com/user-attachments/assets/86e41ef7-0f61-4abe-bb63-ce23dd4cdf1a">

<img width="1176" alt="Screenshot 2024-11-13 at 8 17 38 PM" src="https://github.com/user-attachments/assets/4ad1d4c0-8e5b-437c-99d5-c437cfb8ae6d">

## Disclaimer

Please note that this project is build purely for learning and education purposes. Please be mindful of Netflix's Terms and Condition before attempting any modifications on the script. 
This tool is designed for educational use, and redistribution or public sharing of translated content may violate the Terms and Conditions.

## Contributions

Contributions are always welcome. Please feel free to open new issues or raise a Pull Request for new features or bug fixes.
