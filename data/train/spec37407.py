import numpy as np 

def function(x):

	a5 = 4
	k7 = 9
	paths = []
	try:
		if a5 <= 9:
			k7 = k7/4
			a5 = a5+5
			k7 = 0+9
			paths.append(1)
		else:
			a5 = a5/9
			paths.append(2)
		if x > 7:
			a5 = k7-k7
			k7 = k7*0
			paths.append(3)
		else:
			k7 = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))