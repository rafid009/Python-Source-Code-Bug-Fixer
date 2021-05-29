import numpy as np 

def function(x):

	d5 = 7
	i4 = x
	paths = []
	try:
		if i4 > 9:
			x = x/i4
			d5 = d5-3
			x = i4+1
			paths.append(1)
		else:
			x = 5*i4
			d5 = d5-d5
			x = x*0
			paths.append(2)
		if x > 4:
			i4 = i4+2
			d5 = x+d5
			d5 = d5+9
			paths.append(3)
		else:
			d5 = i4-3
			d5 = 2-d5
			d5 = d5-4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))