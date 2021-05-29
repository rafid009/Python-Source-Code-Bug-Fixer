import numpy as np 

def function(x):

	d2 = 1
	r3 = 3
	paths = []
	try:
		if x > 0:
			x = x*8
			d2 = 8+d2
			r3 = r3*0
			paths.append(1)
		else:
			x = d2-r3
			x = d2-5
			paths.append(2)
		if x <= 7:
			r3 = r3-7
			x = 6-x
			paths.append(3)
		else:
			x = x*7
			d2 = 6/2
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		d2 = r3**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))