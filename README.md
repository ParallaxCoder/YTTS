# <img height="32" width="32" src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/youtube.svg"/> YouTube Transcript Scraper

The YouTube Transcript Scraper is a Python script that allows you to scrape transcripts from multiple YouTube videos in bulk. You can use it in interactive mode by providing YouTube video URLs one by one, or you can provide a list of YouTube video URLs in a text file for batch processing.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Interactive Mode](#interactive-mode)
  - [Batch Mode](#batch-mode)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- Required Python packages (install them using `pip`):
  - `requests`
  - `beautifulsoup4`

### Installation

Clone this repository to your local machine or download the `ytts.py` script:

```shell
git clone https://github.com/your-username/your-repo.git

pip3 install -r requirements.txt
```
## Usage
You can use the YouTube Transcript Scraper in two modes: interactive mode and batch mode.

### Interactive Mode
In interactive mode, you can provide YouTube video URLs one by one. To run the script interactively, simply execute the following command:

```shell
python ytts.py
```

Follow the prompts to input YouTube video URLs. The script will scrape the transcripts one by one.

### Batch Mode
In batch mode, you can provide a list of YouTube video URLs in a text file. To run the script in batch mode, use the `-i` or `--input` flag followed by the path to the text file containing the video URLs:

```shell
python ytts.py -i /path/to/yturls.txt
```

The script will process all the URLs in the text file and scrape the transcripts for each video.

## License

This project is licensed under the GNU General Public License version 3 (GPLv3) - see the [LICENSE](LICENSE) file for details.