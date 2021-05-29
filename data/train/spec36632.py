import numpy as np 

def function(x):

	r5 = x
	r8 = 8
	paths = []
	try:
		if x < 4:
			x = 5+x
			x = 9*9
			paths.append(1)
		else:
			r5 = 7-8
			x = 1/3
			paths.append(2)
		if r8 > 3:
			r8 = r8*6
			r5 = r5-4
			r8 = 7*0
			paths.append(3)
		else:
			x = 7/3
			x = r5/r5
			r5 = x+x
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))