import numpy as np 

def function(x):

	r5 = 2
	k4 = 5
	paths = []
	try:
		if k4 <= 4:
			r5 = r5+0
			r5 = x*0
			r5 = x/3
			paths.append(1)
		else:
			r5 = r5-k4
			r5 = 3/2
			paths.append(2)
		if r5 <= 0:
			k4 = k4/4
			x = x*7
			x = x-5
			paths.append(3)
		else:
			k4 = x/k4
			k4 = k4+r5
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))