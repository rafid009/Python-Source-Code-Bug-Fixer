import numpy as np 

def function(x):

	i2 = x
	w9 = x
	paths = []
	try:
		if i2 > 9:
			w9 = 7*w9
			x = 2+1
			w9 = 4-w9
			paths.append(1)
		else:
			w9 = w9-0
			w9 = 3+i2
			w9 = 5*0
			paths.append(2)
		if i2 < 3:
			i2 = i2/8
			paths.append(3)
		else:
			i2 = i2-5
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))