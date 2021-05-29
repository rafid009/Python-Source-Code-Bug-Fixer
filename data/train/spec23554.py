import numpy as np 

def function(x):

	v9 = x
	k2 = x
	paths = []
	try:
		if v9 <= 4:
			x = x*3
			k2 = k2+5
			paths.append(1)
		else:
			x = x/5
			k2 = 5*8
			x = 7-6
			paths.append(2)
		if k2 >= 6:
			v9 = 4-4
			x = 7*x
			x = x*2
			paths.append(3)
		else:
			k2 = x+x
			v9 = 9+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))