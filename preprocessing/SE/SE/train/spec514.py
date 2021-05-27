import numpy as np 

def function(x):

	d6 = x
	v1 = x
	paths = []
	try:
		if v1 >= 5:
			x = x/4
			d6 = d6*3
			v1 = 0+0
			paths.append(1)
		else:
			d6 = d6-d6
			x = x/5
			x = v1+v1
			paths.append(2)
		if x < 1:
			x = d6+4
			v1 = 2*v1
			x = x*4
			paths.append(3)
		else:
			v1 = d6-2
			d6 = 6+d6
			x = x-7
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		d6 = v1**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))