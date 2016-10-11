from ordered_set import OrderedSet


class FileScrubber():
    excluded_set = {'[Chorus]', '[Chorus:]'}
    min_string_token_count = 2

    def __init__(self, file_name):
        self.file_name = file_name
        self.lines_set = OrderedSet()

    def scrub_file(self):
        with open(self.file_name, 'r') as file_handler:
            line_count = 0
            for line in file_handler:
                line_count += 1
                if not line or line in self.excluded_set or len(line.split()) < self.min_string_token_count:
                    continue
                line = line.strip(' ')
                if not line.endswith(',\n') and line_count % 3 == 0:
                    line = line.replace('\n', '.\n')
                else:
                    line = line.replace('\n', ' ')

                self.lines_set.add(line)

        with open('../scrubbed_file.txt', 'w') as file_handler:
            for item in self.lines_set:
                file_handler.write('{}'.format(item))

if __name__ == "__main__":
    file_scrubber = FileScrubber('../taylor_swift_all_lyrics.txt')
    file_scrubber.scrub_file()