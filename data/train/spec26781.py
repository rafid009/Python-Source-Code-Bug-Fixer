import numpy as np 

def function(x):

	p1 = x
	t3 = 8
	paths = []
	try:
		if x > 1:
			t3 = t3*1
			x = x/3
			paths.append(1)
		else:
			x = 1+7
			t3 = 3+t3
			t3 = 4/t3
			paths.append(2)
		if t3 < 4:
			t3 = t3-4
			p1 = 3-t3
			paths.append(3)
		else:
			x = x*t3
			x = 8/t3
			p1 = p1-5
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