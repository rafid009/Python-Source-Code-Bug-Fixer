import numpy as np 

def function(x):

	b4 = x
	j9 = x
	paths = []
	try:
		if x > 2:
			b4 = b4*6
			x = x/1
			x = b4-x
			paths.append(1)
		else:
			b4 = b4/1
			paths.append(2)
		if j9 <= 6:
			x = 2*x
			paths.append(3)
		else:
			b4 = b4+0
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		b4 = j9**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))