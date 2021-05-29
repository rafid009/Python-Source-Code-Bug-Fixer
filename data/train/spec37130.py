import numpy as np 

def function(x):

	r6 = 1
	f8 = 9
	paths = []
	try:
		if r6 > 8:
			r6 = r6-r6
			x = 5+x
			x = 8*9
			paths.append(1)
		else:
			f8 = f8-x
			paths.append(2)
		if x > 2:
			f8 = f8+1
			f8 = 8-x
			x = 1+x
			paths.append(3)
		else:
			r6 = r6+r6
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		r6 = f8**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))