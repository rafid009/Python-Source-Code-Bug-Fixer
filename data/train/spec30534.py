import numpy as np 

def function(x):

	v8 = x
	j6 = x
	paths = []
	try:
		if x < 2:
			v8 = 9/7
			x = 7+x
			v8 = 0/v8
			paths.append(1)
		else:
			j6 = 8+j6
			x = x*8
			j6 = x+j6
			paths.append(2)
		if x > 8:
			x = 1*2
			j6 = j6-4
			j6 = j6+4
			paths.append(3)
		else:
			x = v8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))