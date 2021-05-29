import numpy as np 

def function(x):

	i7 = 2
	r1 = x
	paths = []
	try:
		if x <= 7:
			i7 = i7*7
			x = x/2
			paths.append(1)
		else:
			r1 = r1/4
			x = 3-x
			i7 = i7*8
			paths.append(2)
		if r1 < 6:
			i7 = 7/2
			paths.append(3)
		else:
			r1 = 1*3
			i7 = i7+r1
			x = r1*0
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))