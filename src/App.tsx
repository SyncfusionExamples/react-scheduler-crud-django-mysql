import React from 'react';
import './App.css';
import { ScheduleComponent, Day, Week, WorkWeek, Month, Agenda, Inject, DragAndDrop, Resize } from '@syncfusion/ej2-react-schedule';
import { DataManager, UrlAdaptor } from '@syncfusion/ej2-data';

function App() {
  
  let dataManager: DataManager = new DataManager({
    url: 'http://127.0.0.1:8000/Home/GetData',
    crudUrl: 'http://127.0.0.1:8000/Home/UpdateData/',
    adaptor: new UrlAdaptor,
    crossDomain: true
  });

  return (
    <ScheduleComponent eventSettings={{ dataSource: dataManager }}>
      <Inject services={[Day, Week, WorkWeek, Month, Agenda, DragAndDrop, Resize]}/>
    </ScheduleComponent>
  );
}

export default App;