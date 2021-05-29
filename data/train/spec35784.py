import numpy as np 

def function(x):

	e9 = x
	r5 = x
	paths = []
	try:
		if e9 > 7:
			e9 = e9*2
			x = x/x
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if r5 >= 9:
			r5 = 1/r5
			r5 = r5*0
			x = e9*r5
			paths.append(3)
		else:
			e9 = 1-e9
			x = x-1
			e9 = 5+e9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))