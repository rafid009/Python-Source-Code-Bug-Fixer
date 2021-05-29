import numpy as np 

def function(x):

	i4 = x
	b3 = x
	paths = []
	try:
		if x > 3:
			b3 = b3/1
			x = 0+i4
			i4 = 3*x
			paths.append(1)
		else:
			b3 = 0/b3
			paths.append(2)
		if i4 < 7:
			i4 = b3*2
			b3 = b3*2
			i4 = 1+x
			paths.append(3)
		else:
			b3 = b3-b3
			x = x-b3
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		b3 = i4**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))