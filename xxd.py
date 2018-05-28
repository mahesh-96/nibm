import argparse

def main():
        parser = argparse.Aargumentpasrse()
        paser.add_argument("file", help="specify A file")
        parser.add_argument("-o","--output", help="print output to terminal"
                                ,action="store_true")
        args = parser.parse_args()

        if args.file:
                offset = 0
                with open(args.file,'rb') as infile:
                        with open(args.file+".dump",'w') as outfile:
                                while true:
                                        chunk = infile.read(16)
                                        if len(chunk)==0:
                                            break

                                        text = str(chunk)
                                        text = ''.join([i if ord(i)<128 and ord(i)>32 \
                                                        else '.' for i in text])

                                        output = "{:#08}".format(offset)+": "
                                        output += " ".join("{:02x}".format(ord(c)) \
                                                          for c in chunk[:8])

                                        if len(chunk) % 16 != 0:
                                                output += "   "*(16-len(chunk))+text

                                        

                                             output += " " + text

                                         if args.output:
                                                 print output
                                         outputfile.write(output + '\n')

                                         offset += 16

      else:
              print parse.usage

if __name__=='__main__':
        main()

                                
