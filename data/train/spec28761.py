import numpy as np 

def function(x):

	k9 = 5
	r6 = x
	paths = []
	try:
		if k9 < 0:
			x = x/3
			paths.append(1)
		else:
			r6 = 7-8
			k9 = k9/9
			paths.append(2)
		if k9 < 3:
			r6 = r6/9
			paths.append(3)
		else:
			k9 = 4+x
			x = x+1
			k9 = k9/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))