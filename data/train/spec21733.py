import numpy as np 

def function(x):

	x6 = 2
	i5 = 9
	paths = []
	try:
		if x <= 7:
			i5 = i5*4
			x6 = x6*2
			x = x+x
			paths.append(1)
		else:
			x6 = x6+x6
			x6 = i5+5
			i5 = 6/3
			paths.append(2)
		if x < 8:
			x = x6/6
			x6 = x6/5
			paths.append(3)
		else:
			i5 = 1+i5
			x6 = x6*x
			x6 = 7-x6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))