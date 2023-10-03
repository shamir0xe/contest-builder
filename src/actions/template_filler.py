from libs.pylib.buffer_io.buffer_reader import BufferReader
from libs.pylib.buffer_io.string_buffer import StringBuffer


def template_filler(template: str, *args: str) -> str:
    reader = BufferReader(StringBuffer(template))
    taken = 0
    page = ""
    while not reader.end_of_buffer():
        line = reader.next_line()
        if taken < len(args):
            cnt = line.count("{}")
            if cnt > 0:
                try:
                    line = line.format(*args[taken:taken+cnt])
                    taken += cnt
                except Exception as e:
                    print(e)
        page += line
    return page
