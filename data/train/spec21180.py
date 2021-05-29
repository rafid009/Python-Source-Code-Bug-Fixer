import numpy as np 

def function(x):

	t1 = x
	m5 = x
	paths = []
	try:
		if x >= 6:
			t1 = t1+0
			m5 = 4*9
			t1 = m5/8
			paths.append(1)
		else:
			t1 = t1*8
			paths.append(2)
		if x < 9:
			t1 = t1-3
			paths.append(3)
		else:
			t1 = x+x
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