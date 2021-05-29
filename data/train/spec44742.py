import numpy as np 

def function(x):

	d6 = x
	i5 = x
	paths = []
	try:
		if i5 <= 5:
			i5 = i5+d6
			i5 = i5/d6
			paths.append(1)
		else:
			d6 = d6-7
			x = x-2
			paths.append(2)
		if x < 2:
			i5 = i5*0
			x = 8+2
			paths.append(3)
		else:
			x = 7/8
			i5 = 5*i5
			d6 = d6*2
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))