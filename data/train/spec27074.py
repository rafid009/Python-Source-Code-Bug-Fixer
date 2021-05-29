import numpy as np 

def function(x):

	t6 = x
	o4 = x
	paths = []
	try:
		if o4 > 2:
			t6 = t6+x
			t6 = 7+t6
			x = x-x
			paths.append(1)
		else:
			t6 = 2/t6
			x = 4+x
			o4 = 7/5
			paths.append(2)
		if x <= 6:
			o4 = o4-o4
			paths.append(3)
		else:
			o4 = o4/5
			t6 = 2+3
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))