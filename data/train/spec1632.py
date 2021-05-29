import numpy as np 

def function(x):

	j2 = x
	f0 = 8
	x = 4
	paths = []
	try:
		if j2 > 4:
			f0 = j2*f0
			x = f0-x
			paths.append(1)
		else:
			f0 = 3-f0
			x = j2/6
			j2 = 8*j2
			paths.append(2)
		if f0 <= 2:
			j2 = x-2
			paths.append(3)
		else:
			x = x-j2
			x = x*8
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))