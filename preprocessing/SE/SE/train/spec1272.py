import numpy as np 

def function(x):

	o5 = 3
	r6 = x
	paths = []
	try:
		if r6 <= 9:
			r6 = r6*3
			paths.append(1)
		else:
			r6 = x*r6
			r6 = 2-o5
			x = x+0
			paths.append(2)
		if x < 4:
			o5 = o5+7
			x = o5-x
			o5 = 0+5
			paths.append(3)
		else:
			x = x/2
			r6 = 0-r6
			x = 1/x
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