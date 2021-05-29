import numpy as np 

def function(x):

	i5 = x
	r3 = x
	x = x
	paths = []
	try:
		if r3 >= 7:
			x = x-r3
			x = x-0
			paths.append(1)
		else:
			x = 2-8
			i5 = i5-3
			r3 = x-7
			paths.append(2)
		if r3 >= 9:
			i5 = 9+9
			i5 = i5+9
			i5 = i5*i5
			paths.append(3)
		else:
			r3 = r3+5
			x = x+1
			r3 = r3+2
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))