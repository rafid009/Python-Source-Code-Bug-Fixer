import numpy as np 

def function(x):

	r5 = 6
	y7 = x
	paths = []
	try:
		if x > 3:
			x = x*0
			r5 = r5-r5
			paths.append(1)
		else:
			r5 = 4-r5
			x = 9+x
			x = x/7
			paths.append(2)
		if y7 > 2:
			y7 = y7*2
			paths.append(3)
		else:
			y7 = 1*2
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