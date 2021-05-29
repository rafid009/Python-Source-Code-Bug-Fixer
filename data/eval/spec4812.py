import numpy as np 

def function(x):

	r8 = x
	b9 = x
	paths = []
	try:
		if b9 < 4:
			b9 = b9/4
			r8 = r8+4
			x = x+7
			paths.append(1)
		else:
			x = x+r8
			paths.append(2)
		if r8 > 9:
			r8 = x+8
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))