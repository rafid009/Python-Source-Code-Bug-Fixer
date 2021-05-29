import numpy as np 

def function(x):

	r6 = x
	b7 = 7
	x = x
	paths = []
	try:
		if r6 > 8:
			x = x+r6
			x = 2+0
			paths.append(1)
		else:
			b7 = x+x
			paths.append(2)
		if b7 >= 2:
			r6 = 0/3
			b7 = 5/b7
			paths.append(3)
		else:
			x = 3/x
			b7 = b7*9
			x = x-6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))