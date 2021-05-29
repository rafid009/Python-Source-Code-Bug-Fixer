import numpy as np 

def function(x):

	t1 = x
	f7 = 2
	x = 4
	paths = []
	try:
		if t1 > 3:
			f7 = 0+9
			paths.append(1)
		else:
			t1 = 5/t1
			t1 = t1*5
			paths.append(2)
		if t1 < 3:
			f7 = f7+7
			f7 = 8+f7
			x = 3+x
			paths.append(3)
		else:
			x = 7-x
			f7 = x*6
			x = x*f7
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))