import numpy as np 

def function(x):

	n2 = x
	b2 = x
	paths = []
	try:
		if b2 < 6:
			n2 = 6*n2
			x = n2*8
			b2 = 4-5
			paths.append(1)
		else:
			x = x+3
			b2 = 7-n2
			b2 = n2/7
			paths.append(2)
		if x > 8:
			x = 0*0
			paths.append(3)
		else:
			b2 = 5+x
			x = n2-8
			b2 = 6+5
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		b2 = b2**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))