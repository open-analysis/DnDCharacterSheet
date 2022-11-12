using DnDCharacterSheet.Core;
using System;

namespace DnDCharacterSheet.MVVM.ViewModel
{
    class MainViewModel : ObservableObject
    {

        public RelayCommand HomeViewCommand { get; set; }
        public RelayCommand DiscoveryViewCommand { get; set; }

        public HomeViewModel homeVM { get; set; }
        public DiscoveryViewModel discoveryVM { get; set; }

        private object _currentView;

        public object CurrentView
        { 
            get { return _currentView; }
            set 
            { 
                _currentView = value; 
                OnPropertyChanged();
            }
        }

        public MainViewModel()
        {
            homeVM = new HomeViewModel();
            discoveryVM = new DiscoveryViewModel();
            CurrentView = homeVM;

            HomeViewCommand = new RelayCommand(o =>
            {
                CurrentView = homeVM;
            });

            DiscoveryViewCommand = new RelayCommand(o =>
            {
                CurrentView = discoveryVM;
            });
        }

    }
}
