import numpy as np 

def function(x):

	d3 = 4
	r7 = x
	paths = []
	try:
		if r7 <= 9:
			d3 = d3*4
			x = x+d3
			d3 = d3+5
			paths.append(1)
		else:
			x = x*9
			r7 = x-r7
			paths.append(2)
		if d3 > 5:
			x = 2+4
			paths.append(3)
		else:
			r7 = r7*7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		d3 = r7**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))