import numpy as np 

def function(x):

	d9 = 8
	t3 = x
	paths = []
	try:
		if t3 > 0:
			d9 = d9+7
			d9 = d9+d9
			x = 5-t3
			paths.append(1)
		else:
			d9 = 3/9
			t3 = 8/3
			paths.append(2)
		if x >= 3:
			d9 = 9/4
			d9 = x/t3
			t3 = x+t3
			paths.append(3)
		else:
			t3 = x+t3
			t3 = x+x
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))