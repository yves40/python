
NUM_ATTEMPTS = 2

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == '1':
                print 'Odd'
            elif i == '0':
                print 'Even'
            else:
                print '*************', i

if __name__ == '__main__':
    transmit_code('0101111')
