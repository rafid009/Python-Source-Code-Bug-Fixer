import numpy as np 

def function(x):

	i9 = 5
	r3 = x
	paths = []
	try:
		if r3 < 0:
			x = 5*i9
			r3 = r3-5
			i9 = i9+8
			paths.append(1)
		else:
			i9 = x*7
			i9 = i9+r3
			r3 = 2-r3
			paths.append(2)
		if i9 > 0:
			x = x-6
			i9 = 1+i9
			r3 = r3+8
			paths.append(3)
		else:
			i9 = 5/i9
			r3 = x/5
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		i9 = r3**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))