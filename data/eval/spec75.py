import numpy as np 

def function(x):

	r3 = x
	i6 = 5
	x = 6
	paths = []
	try:
		if r3 > 3:
			i6 = i6*x
			r3 = 3+r3
			paths.append(1)
		else:
			x = x*2
			r3 = r3/3
			paths.append(2)
		if r3 > 1:
			r3 = r3+3
			i6 = 5+i6
			x = 6*i6
			paths.append(3)
		else:
			r3 = r3/i6
			i6 = i6-i6
			x = x-r3
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		i6 = r3**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))