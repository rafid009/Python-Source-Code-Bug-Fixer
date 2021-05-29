import numpy as np 

def function(x):

	u4 = x
	r5 = 8
	paths = []
	try:
		if u4 <= 5:
			r5 = 2+6
			r5 = r5-u4
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if r5 > 7:
			x = x+r5
			u4 = u4+1
			u4 = 0+u4
			paths.append(3)
		else:
			r5 = r5+4
			r5 = 5-r5
			x = 8-u4
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