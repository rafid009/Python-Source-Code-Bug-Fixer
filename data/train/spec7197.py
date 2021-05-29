import numpy as np 

def function(x):

	t9 = 1
	d6 = x
	paths = []
	try:
		if x < 5:
			x = x*3
			d6 = x*3
			t9 = 2+t9
			paths.append(1)
		else:
			x = 3+2
			t9 = 6+t9
			x = 3+x
			paths.append(2)
		if t9 >= 4:
			t9 = 3/t9
			t9 = 6+t9
			d6 = x+0
			paths.append(3)
		else:
			d6 = x/5
			d6 = 7+d6
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