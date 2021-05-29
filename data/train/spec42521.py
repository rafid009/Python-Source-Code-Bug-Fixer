import numpy as np 

def function(x):

	y7 = 7
	r7 = x
	paths = []
	try:
		if y7 <= 8:
			x = 5*1
			y7 = 8-r7
			paths.append(1)
		else:
			x = 1*8
			x = y7*x
			paths.append(2)
		if r7 < 3:
			y7 = y7/4
			r7 = r7+x
			y7 = y7/3
			paths.append(3)
		else:
			r7 = y7/x
			x = x*0
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))