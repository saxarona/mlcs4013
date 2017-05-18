% Árbol de decisión
% A01170065 Xavier Sánchez
% A00806415 Gabriel González
% Primer árbol

tabla=dlmread("Full.txt");
Y=tabla(:,1);
X=tabla(:,2:7);
Mdl = fitctree(X,Y)

tabla2=dlmread("Full_test.txt");
Y2=tabla2(:,1);
X2=tabla2(:,2:7);

best=0;
level=0;

Ypred=predict(Mdl,X2);
wrong=sum(Ypred~=Y2);
right=sum(Ypred==Y2);
original_accuracy=right/(wrong+right)

for i=0:max(Mdl.PruneList)
    Mdl_prune=prune(Mdl,'level',i);
    Ypred=predict(Mdl_prune,X2);
    wrong=sum(Ypred~=Y2);
    right=sum(Ypred==Y2);
    accuracy=right/(wrong+right);
    if (best < accuracy)
        best=accuracy;
        level=i;
    end
end
best
best-original_accuracy
level
Mdl2=prune(Mdl,'level',level)
view(Mdl2,'Mode','graph')

%Segundo árbol
tabla=dlmread("Full_test.txt");
Y=tabla(:,1);
X=tabla(:,2:7);
Mdl = fitctree(X,Y)

tabla2=dlmread("Full.txt");
Y2=tabla2(:,1);
X2=tabla2(:,2:7);

best=0;
level=0;

Ypred=predict(Mdl,X2);
wrong=sum(Ypred~=Y2);
right=sum(Ypred==Y2);
original_accuracy=right/(wrong+right)

for i=0:max(Mdl.PruneList)
    Mdl_prune=prune(Mdl,'level',i);
    Ypred=predict(Mdl_prune,X2);
    wrong=sum(Ypred~=Y2);
    right=sum(Ypred==Y2);
    accuracy=right/(wrong+right);
    if (best < accuracy)
        best=accuracy;
        level=i;
    end
end
best
best-original_accuracy
level
Mdl2=prune(Mdl,'level',level)
view(Mdl2,'Mode','graph')
