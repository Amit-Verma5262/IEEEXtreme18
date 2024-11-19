import struct
import sys

def main():
    input_data = sys.stdin.read().strip()
    data = input_data.splitlines()

    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        C0 = data[index]
        index += 1
        
        L = int(data[index])
        index += 1
        
        LUTs = []
        for __ in range(L):
            line = data[index].split()
            k_i = int(line[0])
            lut_size = 1 << k_i
            lut_values = line[1:lut_size + 1]
            LUTs.append([hex_to_float(v) for v in lut_values])
            index += 1
        
        Q = int(data[index])
        index += 1
        
        commands_list = []
        for __ in range(Q):
            commands_list.append(data[index])
            index += 1
        
        result = commands(C0, LUTs, commands_list)
        results.append(result)
    
    print('\n'.join(results))

def commands(C0, LUTs, commands):
    C = [C0]
    
    for command in commands:
        parts = command.split()
        cmd_type = parts[0]
        
        if cmd_type == 'L':
            i = int(parts[1])
            j = int(parts[2])
            b = int(parts[3])
            mask = (int(C[0], 16) >> j) & ((1 << b) - 1)
            C.append(LUTs[i][mask])
        
        elif cmd_type == 'N':
            i = int(parts[1])
            j = int(parts[2])
            val1 = int(C[i], 16)
            val2 = int(C[j], 16)
            result = ~(val1 & val2) & 0xFFFFFFFF
            C.append(float_to_hex(struct.unpack('!f', struct.pack('!I', result))[0]))
        
        elif cmd_type == 'F':
            i = int(parts[1])
            j = int(parts[2])
            k = int(parts[3])
            a = hex_to_float(C[i])
            b = hex_to_float(C[j])
            c = hex_to_float(C[k])
            result = a * b + c
            C.append(float_to_hex(result))
        
        elif cmd_type == 'C':
            h = parts[1]
            C.append(h)
    
    return C[-1]

def hex_to_float(hex_value):
    try:
        return struct.unpack('!f', bytes.fromhex(hex_value))[0]
    except (ValueError, struct.error):
        return 0.0

def float_to_hex(float_value):
    try:
        return hex(struct.unpack('!I', struct.pack('!f', float_value))[0])[2:].zfill(8)
    except (ValueError, struct.error):
        return '00000000'

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)