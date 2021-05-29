import numpy as np 

def function(x):

	v4 = x
	i7 = x
	paths = []
	try:
		if x > 7:
			v4 = v4*2
			x = i7-7
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if v4 <= 7:
			i7 = i7+x
			v4 = 0+v4
			i7 = 0-i7
			paths.append(3)
		else:
			i7 = i7/9
			v4 = v4/6
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))