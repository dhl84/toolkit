def remove_newlines(input_filename, output_filename=None):
    with open(input_filename, 'r') as file:
        lines = file.readlines()
    
    processed_lines = []
    paragraph = ""
    
    for line in lines:
        stripped_line = line.strip()
        
        if stripped_line:
            if paragraph:
                paragraph += " " + stripped_line
            else:
                paragraph = stripped_line
        else:
            if paragraph:
                processed_lines.append(paragraph)
                paragraph = ""

    if paragraph:
        processed_lines.append(paragraph)
    
    final_text = "\n\n".join(processed_lines)
    
    if output_filename is None:
        output_filename = input_filename
    
    with open(output_filename, 'w') as file:
        file.write(final_text)

    print(f"Processed text saved to {output_filename}")

# This part allows the script to be run from the command line
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python remove_newlines.py <input_filename> [<output_filename>]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        remove_newlines(input_file, output_file)
