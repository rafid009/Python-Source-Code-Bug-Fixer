import numpy as np 

def function(x):

	d9 = x
	r7 = 4
	x = 5
	paths = []
	try:
		if d9 < 7:
			x = x*1
			x = d9*2
			r7 = r7-4
			paths.append(1)
		else:
			r7 = r7*x
			x = d9+3
			paths.append(2)
		if r7 >= 3:
			r7 = 4+9
			r7 = 2-7
			d9 = 9+6
			paths.append(3)
		else:
			d9 = x*2
			r7 = r7+r7
			x = 6-d9
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		d9 = r7**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))