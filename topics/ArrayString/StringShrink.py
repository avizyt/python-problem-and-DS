import re
import string
from xml.etree.ElementTree import tostring


class StringShrink:
    
    def shrink( str):
        result = []

        count = 0;
        for i in range(len(str)):
            count += 1

            if str[i] != " ":
                if i+1 >= len(str) or str[i] != len(str):
                    result.append(str[i])
                    result.append(count)
            else:
                result.append(str[i])
                count = 0
        
        return " ".join(result)


if __name__ == "__main__":
    str = "abbb vvv rtt rrr eeeee ff x"

    print(StringShrink.shrink(str))
