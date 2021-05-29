import numpy as np 

def function(x):

	b2 = x
	j5 = 6
	paths = []
	try:
		if x >= 4:
			b2 = b2+j5
			x = x*j5
			b2 = b2+4
			paths.append(1)
		else:
			j5 = j5*j5
			j5 = 9+5
			x = 8*3
			paths.append(2)
		if j5 > 9:
			j5 = j5-7
			x = 2+8
			j5 = j5/9
			paths.append(3)
		else:
			j5 = 3-j5
			j5 = 3-b2
			b2 = 2+b2
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